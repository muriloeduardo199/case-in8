from playwright.async_api import async_playwright
import asyncio
from fastapi import FastAPI



app = FastAPI()
 


@app.get("/")
async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
 
        all_items = await page.query_selector_all('.thumbnail')
        lists = []
        for item in all_items:
            lists_not = {}
            name_el = await item.query_selector('h4')
            lists_not['price'] = await name_el.inner_text()
            # price_el = await item.query_selector('.pull-right')
            # lists_not['price'] = await price_el.inner_text()
            stock_el = await item.query_selector('.title')
            lists_not['name'] = await stock_el.inner_text()
            lists.append(lists_not)
        
        # print(lists)
        close_browser =  await browser.close()
        return lists, close_browser
        



    
 
if __name__ == '__main__':
   
    asyncio.run(main())