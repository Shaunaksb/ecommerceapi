import csv
from pymongo import MongoClient
from bson.objectid import ObjectId

def generate_products(db_config):
    # Connect to MongoDB
    client = MongoClient(db_config['url'])
    db = client[db_config['db_name']]
    collection = db[db_config['collection_name']]
    # List of electronic product names
    product_names = [
        "Apple iPhone 13",
        "Samsung Galaxy S21",
        "Sony PlayStation 5",
        "Microsoft Xbox Series X",
        "Apple MacBook Pro",
        "Dell XPS 13",
        "Amazon Echo (4th Gen)",
        "Google Pixel 6",
        "Apple iPad Pro",
        "Samsung Galaxy Tab S7",
        "Bose QuietComfort 35 II",
        "Apple Watch Series 7",
        "Canon EOS M50 Mark II",
        "Nikon D3500",
        "Apple AirPods Pro",
        "Samsung QN90A Neo QLED",
        "LG OLED C1",
        "Sony WH-1000XM4",
        "Apple iMac (24-inch, 2021)",
        "HP Spectre x360 (2021)",
        "Roku Ultra (2020)",
        "Amazon Kindle Paperwhite (2021)",
        "GoPro Hero10 Black",
        "DJI Mavic Air 2",
        "Apple HomePod mini",
        "Samsung Galaxy Z Fold 3",
        "Apple TV 4K (2021)",
        "Sony A8H OLED",
        "JBL Flip 5",
        "Fitbit Charge 4",
        "Ring Video Doorbell Pro 2",
        "Nest Learning Thermostat",
        "Dyson V11 Torque Drive",
        "Instant Pot Duo Nova",
        "iRobot Roomba S9+",
        "Philips Sonicare ProtectiveClean 6100",
        "Garmin Forerunner 245",
        "Anker Soundcore Liberty Air 2 Pro",
        "Logitech MX Master 3",
        "WD Black SN850 NVMe SSD",
        "Netgear Nighthawk AX12",
        "TP-Link Archer AX6000",
        "Asus ROG Rapture GT-AX11000",
        "Eero Pro 6",
        "Google Nest Wifi",
        "Linksys Velop MX10",
        "Netgear Orbi WiFi 6",
        "TP-Link Deco X60",
        "Asus ZenWiFi AX6600",
        "Arris Surfboard Max Pro"
    ]

    # Generate 50 electronic products
    for i in range(50):
        product = {
            'name': product_names[i % len(product_names)],  # Use modulo to cycle through product names
            'price': i * 10,
            'quantity': i * 5
        }
        collection.insert_one(product)

    # Query the collection to get all products
    products = collection.find()

    # Write the products to a CSV file
    with open('products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product ID', 'Product Name', 'Product Price', 'Product Available Quantity'])
        for product in products:
            writer.writerow([str(product['_id']), product['name'], product['price'], product['quantity']])