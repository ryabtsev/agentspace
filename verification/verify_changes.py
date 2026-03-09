import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load the local index.html file
        file_path = f"file://{os.getcwd()}/index.html"
        await page.goto(file_path)

        # Take screenshots
        await page.screenshot(path="verification/index_verification.png", full_page=True)

        # Check for specific text
        header_text = await page.inner_text("header h1")
        print(f"Header: {header_text}")

        subtitle_text = await page.inner_text(".subtitle")
        print(f"Subtitle: {subtitle_text}")

        tags = await page.inner_text("header .tag")
        print(f"Tags: {tags}")

        # Targeted screenshot of the new section
        adaptability_card = page.locator(".card:has-text('Structure Adaptability')")
        if await adaptability_card.count() > 0:
            await adaptability_card.screenshot(path="verification/adaptability_section.png")
            print("Captured adaptability section screenshot.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
