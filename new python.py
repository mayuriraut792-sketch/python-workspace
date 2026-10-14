
def calculateProductTotal(a, b, c, d):
    return (a * b) + (c * d)


def calculateGST(amount):
    gst = amount * 18 / 100
    return amount + gst
def calculateDeliveryCharge():
    return 100

def calculateCouponDiscount(amount):
    discount = amount * 10 / 100
    
    return discount


def calculateOrderTotal(a, b, c, d):
    products = calculateProductTotal(a, b, c, d)

    total_with_gst = calculateGST(products)

    delivery = calculateDeliveryCharge()
    amount = total_with_gst + delivery

    discount = calculateCouponDiscount(amount)

    return amount - discount


def calculateRefund(price, quantity):
    amount = price * quantity
    gst = amount * 18 / 100

    return amount + gst


def calculateFinalBill(a, b, c, d):
    products = calculateProductTotal(a, b, c, d)

    gst_amount = calculateGST(products)
    gst = gst_amount - products

    delivery = calculateDeliveryCharge()

    amount = gst_amount + delivery

    discount = calculateCouponDiscount(amount)

    payable = calculateOrderTotal(a, b, c, d)

    print(f"Product Total = {products:.2f}")
    print(f"GST (18%) = {gst:.2f}")
    print(f"Delivery Charge = {delivery:.2f}")
    print(f"Amount Before Discount = {amount:.2f}")
    print(f"Coupon Discount = {discount:.2f}")
    print(f"Final Payable Amount = {payable:.2f}")

    return payable

calculateFinalBill(50000, 1, 2000, 2)
