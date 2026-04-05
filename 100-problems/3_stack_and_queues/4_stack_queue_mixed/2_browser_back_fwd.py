# History: Google → YouTube → Reddit
# You hit back twice → now on Google
# You visit Twitter.
# Can you forward? - NO

class Browser:
    def __init__(self):
        self.current_url = None
        self.back_stack = []
        self.fwd_stack = []

    def visit(self, url):
        if self.current_url:
            self.back_stack.append(self.current_url)
            self.fwd_stack = []
            self.current_url = url
        else:
            self.current_url = url

    def back(self):
        if self.back_stack:
            self.fwd_stack.append(self.current_url)
            self.current_url = self.back_stack.pop()

    def forward(self):
        if self.fwd_stack:
            self.back_stack.append(self.current_url)
            self.current_url = self.fwd_stack.pop()

    def __repr__(self):
        return(f"Current url = {self.current_url}, Back Stack = {self.back_stack}, Fwd stack = {self.fwd_stack}")

b = Browser()
b.visit("google.com")
b.visit("youtube.com")
b.visit("reddit.com")
print(b.current_url)  # reddit.com
b.back()
print(b.current_url)  # youtube.com
b.back()
print(b.current_url)  # google.com
b.forward()
print(b.current_url)  # youtube.com
b.visit("twitter.com")
print(b.current_url)  # twitter.com
b.forward()
print(b.current_url)  # should still be twitter.com (forward cleared!)
b.back()
print(b.current_url)  # youtube.com