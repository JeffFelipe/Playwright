from playwright.sync_api import sync_playwright



path_to_extension = F"C:/Users\'YOU USER'\AppData\Local\Google\Chrome/User Data\Default\Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.20.0_0"
user_data_dir = "C:/Users\'YOU USER'\AppData\Local\Google\Chrome/User Data\Default"


def run(playwright):

    browser = playwright.chromium.launch_persistent_context(
        user_data_dir,
        locale='pt-BR',
        headless=False,
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )

    context = browser
    page = browser.new_page()

    page.goto('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
    page.locator('//html/body/div[1]/div/div[3]/div/div/form/div/div/input').fill('YOU PASSWORD')


    page.reload()


