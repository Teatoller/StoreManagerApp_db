class ProductModel():
    """ Constructor model for our PRODUCTS """
    product_id = 1

    def __init__(self, name, price, quantity, category):
        """ Declaring variable to be used within the class  """
        self.product_id = ProductModel.product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        ProductModel.product_id += 1

    def resultant(self):
        """ Outlines format by which product(s) are returned"""
        return dict(
            product_name=self.name,
            product_price=self.price,
            product_quantity=self.quantity,
            product_category=self.category
        )


class ListDatabase():
    """ Database Model for methods """
   
    PRODUCTS = []
    SALES = []
    USERS = []

   
    @classmethod
    def get_product_by_name(cls, name):
        """ Iterates and loops and returns all products in PRODUCT list """
        for product in cls.PRODUCTS:
            if product.name == name:
                return product

    @classmethod
    def get_product_id(cls, product_id):
        """ Iterates and loops PRODUCTS return the product """
        for product in cls.PRODUCTS:
            if product.product_id == product_id:
                return product
