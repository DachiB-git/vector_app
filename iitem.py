class StockItem:
    def __init__(self, ID, W_NAME, UNIT_ID, QUANTITY, PRICE, AMOUNT, BAR_CODE, A_ID, VAT_TYPE, STATUS):
        self.ID = ID
        self.W_NAME = W_NAME

        match UNIT_ID:
            case "1":
                self.UNIT_ID = "ცალი"
            case "2":
                self.UNIT_ID = "კგ"
            case "3":
                self.UNIT_ID = "გრამი"
            case "4":
                self.UNIT_ID = "ლიტრი"
            case "5":
                self.UNIT_ID = "ტონა"
            case "7":
                self.UNIT_ID = "სანტიმეტრი"
            case "8":
                self.UNIT_ID = "მეტრი"
            case "9":
                self.UNIT_ID = "კილომეტრი"
            case "10":
                self.UNIT_ID = "კვ.სმ"
            case "11":
                self.UNIT_ID = "კვ.მ"
            case "12":
                self.UNIT_ID = "მ^3"
            case "13":
                self.UNIT_ID = "მილილიტრი"
            case "14":
                self.UNIT_ID = "შეკვრა"
            case _:
                self.UNIT_ID = "სხვა"
        self.QUANTITY = QUANTITY
        self.PRICE = PRICE
        self.AMOUNT = AMOUNT
        self.BAR_CODE = BAR_CODE
        self.A_ID = A_ID
        match VAT_TYPE:
            case 0:
                self.VAT_TYPE = "ჩვეულებრივი"
            case 1:
                self.VAT_TYPE = "ნულოვანი"
            case 2:
                self.VAT_TYPE = "დაუბეგრავი"
            case _:
                self.VAT_TYPE = "ჩვეულებრივი"
        self.STATUS = STATUS

    def __str__(self):
        return f"ID : {self.ID}\n" \
               f"W_NAME : {self.W_NAME}\n" \
               f"UNIT_ID : {self.UNIT_ID}\n" \
               f"QUANTITY : {self.QUANTITY}\n" \
               f"PRICE : {self.PRICE}\n" \
               f"AMOUNT : {self.AMOUNT}\n" \
               f"BAR_CODE : {self.BAR_CODE}\n" \
               f"A_ID : {self.A_ID}\n" \
               f"VAT_TYPE : {self.VAT_TYPE}\n" \
               f"STATUS : {self.STATUS}"

    def to_list_csv(self):
        return [self.BAR_CODE, self.W_NAME, self.ID, self.QUANTITY, self.PRICE, self.AMOUNT, self.VAT_TYPE]

    def __eq__(self, other):
        return self.W_NAME == other.W_NAME and self.ID == other.ID and self.PRICE == other.PRICE and \
            self.BAR_CODE == other.BAR_CODE and self.A_ID == other.A_ID \
            and self.VAT_TYPE == other.VAT_TYPE and self.STATUS == other.STATUS
