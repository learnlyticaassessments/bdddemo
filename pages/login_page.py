class LoginPage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def open(self):
        self.page.goto(self.base_url, wait_until="domcontentloaded")

    def login(self, username: str, password: str):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def is_dashboard_visible(self) -> bool:
        # On SauceDemo, successful login shows inventory container
        return self.page.is_visible("#inventory_container")
