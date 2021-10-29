from App.DB import DB


class Product:
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        return [
            {
                "id": 1,
                "name": "Triumph Street Triple 765RS",
                "price": 58000
            },
            {
                "id": 2,
                "name": "Yamaha YZF-R6",
                "price": 40000
            }
        ]
