class solution(object):
    def generateparenthesis(self,n):
        result=[]
        self.generateparenthesisUtil(n,n,"",result)
        return result
    def generateparenthesisUtil(self,left,right,temp,result):
        if left==0 and right==0:
            result.append(temp)
            return
        if left>0:
            self.generateparenthesisUtil(left-1,right,temp+'(',result)
        if right>left:
           self.generateparenthesisUtil(left,right-1,temp+')',result)
ob=solution()
print(ob.generateparenthesis(4))
            
