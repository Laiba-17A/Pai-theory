
print("Name: Laiba Javed")
print("ID: 24K-0014")
print("============================= Question 1 =========================")
print(" ")

#The raW LOg Of all items in all Orders
transactionLog = [
{'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_10'},
{'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_12'},
{'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_10'},
{'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_15' },
{'orderId': 1003, 'customerId': 'cust_Ahmed', 'productId': 'prod_15'},
{'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_12'},
{'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_10' }
]

# The mapping of product IDs to names
productcatalog = {
'prod_10': 'Wireless Mouse',
'prod_12': 'Keyboard',
'prod_15': 'USB-C Hub',
}

#task1: transform data
def processTransactions(transactionlist):
    custdict = {}
    for t in transactionlist:
        c_id=t['customerId']
        p_id=t['productId']
        
        x=0
        for c in custdict.keys():
            if c==c_id:
                x=1
                
        if x==0:
            custdict[c_id]=[]
            
        custdict[c_id].append(p_id)

    return custdict

#task2: find pairs
def findFrequentPairs(customerData):
    pairdict = {}
    for c in customerData.keys():      
        prod = customerData[c]  #list of products
        #print(prod)
        n=len(prod)
        for i in range(n):
            
            for j in range(i+1,n):
                if(i==j):
                    continue
                pair = tuple(sorted([prod[i], prod[j]]))  #sort the tuple for duplicates
                if pair in pairdict:
                    pairdict[pair] +=1
                else:
                    pairdict[pair] = 1

    
    return pairdict

#task 3: get recommendation and output ranked list
def getRecommendations(targetProductId, frequentPairs):
    recom_list= []
    for a, b in frequentPairs:
        if targetProductId == a:
            recom_list.append((b, frequentPairs[(a, b)]))
        elif targetProductId == b:
            recom_list.append((a, frequentPairs[(a, b)]))
    
    #sort by frequency
    def get_freq(x):
        return x[1]

    recom_list.sort(key=get_freq, reverse=True)

    return recom_list

#task 4: generate report
def generateReport(targetProductId, recommendations, Catalog):
    print("Recommendations for product: " ,Catalog[targetProductId])
    print("Ranked Recommendations:")

    for i, rec in enumerate(recommendations, start=1):
        prod_id = rec[0]
        freq = rec[1]
        print(str(i) + ". " + Catalog[prod_id] + " (bought together " + str(freq) + " times)")

#main
a=processTransactions(transactionLog)
print("customer purchase: ",a)
print("")
b=findFrequentPairs(a)
print("frequent pairs: ",b)
print("")

c=getRecommendations('prod_12', b)
generateReport('prod_12', c, productcatalog)
print("")