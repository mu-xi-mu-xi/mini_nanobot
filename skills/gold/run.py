import requests

def run(arguments: dict):

    currency = arguments.get("currency", "CNY")

    try:
        url = "https://api.gold-api.com/price/XAU"

        response = requests.get(url)
        data = response.json()

        price = data.get("price")

        if currency == "CNY":
            # 简单汇率估算
            price_cny = price * 7.2
            return f"当前黄金价格约为 {price_cny:.2f} CNY/盎司"
        
        elif currency == "RMB":
            price_rmb = price * 7.2
            return f"当前黄金价格约为 {price_rmb:.2f} RMB"
        else:
            return f"当前黄金价格约为 {price} {currency}/盎司"

    except Exception as e:
        return f"获取黄金价格失败: {str(e)}"

