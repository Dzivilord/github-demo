

class Custom:
    def __init__(self,idAccount,name,address,typeSaving,identify,openDate):
        self.idAccount=idAccount
        self.name=name
        self.address=address
        self.typeSaving=typeSaving
        self.identify=identify
        self.openDate=openDate
    

class Solution:
    pass

Loi=Custom(23,"Gaylord",'DN City','12 months','22120188','17/9/2024')
print(Loi.address)

print (Loi.name)
print(Loi.openDate)
