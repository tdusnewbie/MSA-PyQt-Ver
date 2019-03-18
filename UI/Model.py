import sqlite3


class User:
    def __init__(self, name = None, username = None, passWord = None):
        self.name = name
        self.username = username
        self.passWord = passWord


class Item:
    def __init__(self, name = None, idItem = None, listType = None):
        self.name = name
        self.idItem = idItem
        self.listType = listType


class TypeItem:
    def __init__(self,  name = None,        idType = None,      idParent = None,
                        amount = None,      unitPrice = None,   wholePrice = None,
                        originPrice = None, imagePath = None,   notice = None):
        self.name = name
        self.idType = idType
        self.idParent = idParent
        self.amount = amount
        self.unitPrice = unitPrice
        self.wholePrice = wholePrice
        self.originPrice = originPrice
        self.imagePath = imagePath
        self.notice = notice


class Bill:
    def __init__(self,  nameItem = None,    nameType = None,    idBill = None,
                        amount = None,      saleType = None,    price = None,
                        createdDate = None, createdTime = None, createdUser = None,
                        notice = None):
        
        self.nameItem = nameItem
        self.nameType = nameType
        self.idBill = idBill
        self.amount = amount
        self.saleType = saleType
        self.price = price
        self.createdDate = createdDate
        self.createdTime = createdTime
        self.createdUser = createdUser
        self.notice = notice



class Database:
    def __init__(self):
        self.data = sqlite3.connect("./Data/data.db")
        self.createTable()

    # Create Table in Database method
    def createTable(self):
        cursor = self.data.cursor()
        BillTable = """
        CREATE TABLE IF NOT EXISTS Bill(
            itemName    TEXT,
            typeName    TEXT,
            idBill      TEXT,
            amount      INTEGER,
            saletype    TEXT,
            price       REAL,
            createdDate TEXT,
            createdTime TEXT,
            createdUser TEXT,
            notice      TEXT
        );"""
        
        UserTable = """
        CREATE TABLE IF NOT EXISTS User(
            name        TEXT,
            username    TEXT NOT NULL,
            passWord    TEXT,
            PRIMARY KEY(username)
        );"""

        ItemTable = """
        CREATE TABLE IF NOT EXISTS Item(
            name        TEXT,
            idItem      TEXT NOT NULL,
            PRIMARY KEY(idItem)
        );"""

        TypeItemTable = """
        CREATE TABLE IF NOT EXISTS TypeItem(
            name        TEXT,
            idType      TEXT NOT NULL,
            idParent    TEXT,
            amount      INTEGER,
            unitPrice   REAL,
            wholePrice  REAL,
            originPrice REAL,
            imagePath   TEXT,
            notice      TEXT,
            PRIMARY KEY(idType)
        );"""

        cursor.execute(UserTable)
        cursor.execute(ItemTable)
        cursor.execute(TypeItemTable)
        cursor.execute(BillTable)

    def closeDatabase(self):
        self.data.close()

    # Insert new value into database method
    def insertUser(self, user):
        cursor = self.data.cursor()
        cursor.execute("INSERT INTO User (name, username, passWord) VALUES (?,?,?)",
                        (user.name, user.username, user.passWord))
        self.data.commit()
        cursor.close()

    def insertItem(self, item):
        cursor = self.data.cursor()
        cursor.execute("INSERT INTO Item (name, idItem) VALUES (?,?)",
                        (item.name, item.idItem))
        self.data.commit()
        cursor.close()

    def insertTypeItem(self, typeItem):
        cursor = self.data.cursor()
        cursor.execute("""INSERT INTO TypeItem (name,
                                                idType, 
                                                idParent, 
                                                amount, 
                                                unitPrice, 
                                                wholePrice,
                                                originPrice,
                                                imagePath,
                                                notice) VALUES (?,?,?,?,?,?,?,?,?)""",
                        (typeItem.name, typeItem.idType, typeItem.idParent,
                        typeItem.amount, typeItem.unitPrice, typeItem.wholePrice,
                        typeItem.originPrice, typeItem.imagePath, typeItem.notice))
        self.data.commit()
        cursor.close()

    def insertBill(self, bill):
        cursor = self.data.cursor()
        cursor.execute("""INSERT INTO Bill (itemName,
                                            typeName, 
                                            idBill, 
                                            amount, 
                                            saleType, 
                                            price,
                                            createdDate,
                                            createdTime,
                                            createdUser,
                                            notice) VALUES (?,?,?,?,?,?,?,?,?,?)""",
                        (bill.nameItem, bill.nameType, bill.idBill,
                        bill.amount, bill.saleType, bill.price, 
                        bill.createdDate, bill.createdTime, bill.createdUser, 
                        bill.notice))
        self.data.commit()
        cursor.close()

    # Delete value in database method 
    def deleteUser(self, username):
        cursor = self.data.cursor()
        cursor.execute("DELETE FROM User WHERE username = ?",(username,))
        self.data.commit()
        cursor.close()

    def deleteItem(self, idItem):
        cursor = self.data.cursor()
        cursor.execute("DELETE FROM Item WHERE idItem = ?",(idItem,))
        self.deleteAllTypeHasIDParent(idItem)
        self.data.commit()
        cursor.close()

    def deleteAllTypeHasIDParent(self, idParent):
        cursor = self.data.cursor()
        cursor.execute("DELETE FROM TypeItem WHERE idParent = ?",(idParent,))
        self.data.commit()
        cursor.close()
    
    def deleteTypeItem(self, idType):
        cursor = self.data.cursor()
        cursor.execute("DELETE FROM TypeItem WHERE idType = ?",(idType,))
        self.data.commit()
        cursor.close()
    
    # Get List/Value from database method
    def getListUser(self):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM User")
        listUser = []
        for row in cursor.fetchall():
            user = User(name = row[0], username = row[1], passWord = row[2])
            listUser.append(user)

        return listUser

    def getUserInfo(self, username):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM User WHERE username = ?",(username,))
        user = User()
        for row in cursor.fetchall():
            user.name = row[0]
            user.username = row[1]
            user.passWord = row[2]
        return user

    ####### All Get List Item Method #######

    def getListItem(self):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Item")
        listItem = []
        for row in cursor.fetchall():
            item = Item(name = row[0], idItem = row[1])
            listType = self.getListTypeHasIDParent(item.idItem)
            item.listType = listType
            listItem.append(item)

        return listItem

    def getListItemWithoutType(self):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Item")
        listItem = []
        for row in cursor.fetchall():
            item = Item(name = row[0], idItem = row[1])
            listItem.append(item)

        return listItem

    def getListItemWithName(self,itemName):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Item WHERE name LIKE ?",("%" + itemName + "%",))
        listItem = []
        for row in cursor.fetchall():
            item = Item(name = row[0], idItem = row[1])
            listType = self.getListTypeHasIDParent(item.idItem)
            item.listType = listType
            listItem.append(item)

        return listItem

    def getListItemWithID(self, idItem):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Item WHERE idItem LIKE ?",("%" + idItem + "%",))
        listItem = []
        for row in cursor.fetchall():
            item = Item(name = row[0], idItem = row[1])
            listType = self.getListTypeHasIDParent(item.idItem)
            item.listType = listType
            listItem.append(item)

        return listItem

    ####### All Get List Type Item Method #######
    def getListTypeHasIDParent(self, idParent):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM TypeItem WHERE idParent = ?",(idParent,))
        listType = []
        for row in cursor.fetchall():
            typeItem = TypeItem(name = row[0], idType= row[1], idParent= row[2],
                                amount = row[3], unitPrice= row[4], wholePrice= row[5],
                                originPrice= row[6], imagePath= row[7], notice= row[8])
            listType.append(typeItem)

        return listType

    def getAllListType(self):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM TypeItem")
        listType = []
        for row in cursor.fetchall():
            typeItem = TypeItem(name = row[0], idType= row[1], idParent= row[2],
                                amount = row[3], unitPrice= row[4], wholePrice= row[5],
                                originPrice= row[6], imagePath= row[7], notice= row[8])
            listType.append(typeItem)

        return listType

    def getListTypeWithName(self, nameType):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM TypeItem WHERE name LIKE ?",("%" + nameType + "%",))
        listType = []
        for row in cursor.fetchall():
            typeItem = TypeItem(name = row[0], idType= row[1], idParent= row[2],
                                amount = row[3], unitPrice= row[4], wholePrice= row[5],
                                originPrice= row[6], imagePath= row[7], notice= row[8])
            listType.append(typeItem)

        return listType
    
    def getListTypeWithID(self, idType):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM TypeItem WHERE idType LIKE ?",("%" + idType + "%",))
        listType = []
        for row in cursor.fetchall():
            typeItem = TypeItem(name = row[0], idType= row[1], idParent= row[2],
                                amount = row[3], unitPrice= row[4], wholePrice= row[5],
                                originPrice= row[6], imagePath= row[7], notice= row[8])
            listType.append(typeItem)

        return listType
    
    def getListTypeWithAmount(self, amount):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM TypeItem WHERE amount LIKE ?",("%" + amount + "%",))
        listType = []
        for row in cursor.fetchall():
            typeItem = TypeItem(name = row[0], idType= row[1], idParent= row[2],
                                amount = row[3], unitPrice= row[4], wholePrice= row[5],
                                originPrice= row[6], imagePath= row[7], notice= row[8])
            listType.append(typeItem)

        return listType

    def getListTypeWithUnitPrice(self, unitPrice):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM TypeItem WHERE unitPrice LIKE ?",("%" + unitPrice + "%",))
        listType = []
        for row in cursor.fetchall():
            typeItem = TypeItem(name = row[0], idType= row[1], idParent= row[2],
                                amount = row[3], unitPrice= row[4], wholePrice= row[5],
                                originPrice= row[6], imagePath= row[7], notice= row[8])
            listType.append(typeItem)

        return listType
    
    def getListTypeWithWholePrice(self, wholePrice):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM TypeItem WHERE wholePrice LIKE ?",("%" + wholePrice + "%",))
        listType = []
        for row in cursor.fetchall():
            typeItem = TypeItem(name = row[0], idType= row[1], idParent= row[2],
                                amount = row[3], unitPrice= row[4], wholePrice= row[5],
                                originPrice= row[6], imagePath= row[7], notice= row[8])
            listType.append(typeItem)

        return listType
    
    def getListTypeWithOriginPrice(self, originPrice):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM TypeItem WHERE originPrice LIKE ?",("%" + originPrice + "%",))
        listType = []
        for row in cursor.fetchall():
            typeItem = TypeItem(name = row[0], idType= row[1], idParent= row[2],
                                amount = row[3], unitPrice= row[4], wholePrice= row[5],
                                originPrice= row[6], imagePath= row[7], notice= row[8])
            listType.append(typeItem)

        return listType

    def getListTypeWithImagePath(self, imagePath):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM TypeItem WHERE imagePath LIKE ?",("%" + imagePath + "%",))
        listType = []
        for row in cursor.fetchall():
            typeItem = TypeItem(name = row[0], idType= row[1], idParent= row[2],
                                amount = row[3], unitPrice= row[4], wholePrice= row[5],
                                originPrice= row[6], imagePath= row[7], notice= row[8])
            listType.append(typeItem)

        return listType

    def getListTypeWithNotice(self, notice):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM TypeItem WHERE notice LIKE ?",("%" + notice + "%",))
        listType = []
        for row in cursor.fetchall():
            typeItem = TypeItem(name = row[0], idType= row[1], idParent= row[2],
                                amount = row[3], unitPrice= row[4], wholePrice= row[5],
                                originPrice= row[6], imagePath= row[7], notice= row[8])
            listType.append(typeItem)

        return listType

    ####### All Get List Bill Method #######
    def getListBillAtDate(self, inputDate):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill WHERE createdDate like ?",("%"+inputDate + "%",))
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill
    
    def getListBillWithItemName(self, itemName):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill WHERE itemName like ?",("%"+itemName + "%",))
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill

    def getListBillWithTypeName(self, typeName):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill WHERE typeName like ?",("%"+typeName+"%",))
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill

    def getListBillWithIDBill(self, idBill):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill WHERE idBill like ?",("%"+idBill + "%",))
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill

    def getListBillWithAmount(self, amount):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill WHERE amount like ?",("%"+amount+"%",))
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill

    def getListBillWithSaleType(self, saleType):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill WHERE saleType like ?",("%"+saleType+"%",))
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill

    def getListBillWithPrice(self, price):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill WHERE price like ?",("%"+price+"%",))
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill

    def getListBillAtTime(self,createdTime):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill WHERE createdTime like ?",("%"+createdTime+"%",))
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill

    def getListBillWithUserCreate(self, createdUser):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill WHERE createdUser like ?",("%"+createdUser+"%",))
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill

    def getListBillWithNotice(self, notice):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill WHERE notice like ?",("%"+notice+"%",))
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill

    def getAllListBill(self):
        cursor = self.data.cursor()
        cursor.execute("SELECT * FROM Bill")
        listBill = []
        for row in cursor.fetchall():
            bill = Bill(nameItem= row[0], nameType= row[1], idBill= row[2],
                        amount= row[3], saleType= row[4], price= row[5],
                        createdDate= row[6], createdTime= row[7], createdUser= row[8],
                        notice= row[9])
            listBill.append(bill)
        
        return listBill

    # Update value in database method
    ###### Type Item Update Method ######
    def updateTypeName(self, idType, newName):
        cursor = self.data.cursor()
        cursor.execute("UPDATE TypeItem SET name = ? WHERE idType = ?",(newName,idType))
        self.data.commit()
        cursor.close()
    
    def updateTypeID(self, idType, newID):
        cursor = self.data.cursor()
        cursor.execute("UPDATE TypeItem SET idType = ? WHERE idType = ?",(newID,idType))
        self.data.commit()
        cursor.close()

    def updateAllTypeHasIDParent(self, idParent):
        cursor = self.data.cursor()
        cursor.execute("UPDATE TypeItem SET idParent = ? WHERE idParent = ?",(idParent,idParent))
        self.data.commit()
        cursor.close()

    def updateTypeAmount(self, idType, newAmount):
        cursor = self.data.cursor()
        cursor.execute("UPDATE TypeItem SET amount = ? WHERE idType = ?",(int(newAmount),idType))
        self.data.commit()
        cursor.close()

    def updateTypeUnitPrice(self, idType, newUnitPrice):
        cursor = self.data.cursor()
        cursor.execute("UPDATE TypeItem SET unitPrice = ? WHERE idType = ?",(float(newUnitPrice),idType))
        self.data.commit()
        cursor.close()

    def updateTypeWholePrice(self, idType, newWholePrice):
        cursor = self.data.cursor()
        cursor.execute("UPDATE TypeItem SET wholePrice = ? WHERE idType = ?",(float(newWholePrice),idType))
        self.data.commit()
        cursor.close()

    def updateTypeOriginPrice(self, idType, newOriginPrice):
        cursor = self.data.cursor()
        cursor.execute("UPDATE TypeItem SET originPrice = ? WHERE idType = ?",(float(newOriginPrice),idType))
        self.data.commit()
        cursor.close()
    
    def updateTypeNotice(self, idType, newNotice):
        cursor = self.data.cursor()
        cursor.execute("UPDATE TypeItem SET notice = ? WHERE idType = ?",(newNotice,idType))
        self.data.commit()
        cursor.close()

    def updateTypeImagePath(self, idType, newPath):
        cursor = self.data.cursor()
        cursor.execute("UPDATE TypeItem SET imagePath = ? WHERE idType = ?",(newPath,idType))
        self.data.commit()
        cursor.close()

    ###### Item Update Method ######
    def updateItemName(self, idItem, newName):
        cursor = self.data.cursor()
        cursor.execute("UPDATE Item SET name = ? WHERE idItem = ?",(newName,idItem))
        self.data.commit()
        cursor.close()

    def updateItemID(self, idItem, newID):
        cursor = self.data.cursor()
        cursor.execute("UPDATE Item SET idItem = ? WHERE idItem = ?",(newID,idItem))
        self.data.commit()
        cursor.close()

    ###### User Update Method ######
    def updateNameOfUser(self, username, newName):
        cursor = self.data.cursor()
        cursor.execute("UPDATE User SET name = ? WHERE username = ?",(newName,username))
        self.data.commit()
        cursor.close()

    def updatePassOfUser(self, username, newPass):
        cursor = self.data.cursor()
        cursor.execute("UPDATE User SET passWord = ? WHERE username = ?",(newPass,username))
        self.data.commit()
        cursor.close()
