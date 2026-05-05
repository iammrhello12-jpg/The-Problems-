import os
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

# Add src to path to import agent
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from agent.model import SimpleAgent

class ChatBubble(Label):
    def __init__(self, text, sender, **kwargs):
        super().__init__(text=text, **kwargs)
        self.size_hint_y = None
        self.text_size = (Window.width * 0.7, None)
        self.padding = (10, 10)
        self.halign = 'right' if sender == 'user' else 'left'
        self.color = (1, 1, 1, 1) if sender == 'user' else (0, 0, 0, 1)

        # Simple background color simulation
        with self.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            if sender == 'user':
                Color(0.0, 0.48, 1.0, 1) # Blue
            else:
                Color(0.91, 0.92, 0.94, 1) # Light Grey
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[(10, 10), (10, 10), (2, 2), (10, 10)])

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.height = self.texture_size[1] + 20

class AIApp(App):
    def build(self):
        self.title = "AI Agent Assistant"

        # Initialize Agent
        self.agent = SimpleAgent()
        base_path = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_path, "..", "..", "model.joblib")
        data_path = os.path.join(base_path, "..", "..", "data", "intents.csv")

        if os.path.exists(model_path):
            self.agent.load(model_path)
        elif os.path.exists(data_path):
            self.agent.train(data_path)

        # Layouts
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.scroll = ScrollView(size_hint=(1, 0.85))
        self.chat_list = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.chat_list.bind(minimum_height=self.chat_list.setter('height'))
        self.scroll.add_widget(self.chat_list)

        input_area = BoxLayout(size_hint=(1, 0.15), spacing=10)
        self.message_input = TextInput(hint_text="Type your message...", multiline=False)
        send_btn = Button(text="Send", size_hint=(0.2, 1), background_color=(0.0, 0.48, 1.0, 1))
        send_btn.bind(on_press=self.send_message)

        input_area.add_widget(self.message_input)
        input_area.add_widget(send_btn)

        root.add_widget(self.scroll)
        root.add_widget(input_area)

        # Initial greeting
        self.add_bubble("Hello! I am your AI assistant. How can I help you today?", 'agent')

        return root

    def add_bubble(self, text, sender):
        bubble = ChatBubble(text=text, sender=sender)
        self.chat_list.add_widget(bubble)
        Clock.schedule_once(lambda dt: setattr(self.scroll, 'scroll_y', 0), 0.1)

    def send_message(self, instance):
        text = self.message_input.text.strip()
        if not text:
            return

        self.add_bubble(text, 'user')
        self.message_input.text = ""

        # Predict
        result = self.agent.predict(text)
        self.add_bubble(result['response'], 'agent')

if __name__ == "__main__":
    AIApp().run()
