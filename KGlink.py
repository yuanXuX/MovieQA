#-*- coding: UTF-8 -*-
# @Time    : 2019/4/12 19:53
# @Author  : xiongzongyang
# @Site    : 
# @File    : query.py
# @Software: PyCharm

from py2neo import Graph,Node,Relationship,NodeMatcher

class Query():
    def __init__(self):
        self.graph=Graph("http://localhost:7474", username="neo4j",password="neo4jxy")
    def run(self,cql):
        result=[]
        find_rela = self.graph.run(cql)
        for i in find_rela:
            result.append(i.items()[0][1])
        return result




# if __name__ == '__main__':
#     SQL=Query()
#     result=SQL.run("match (m:Movie)-[]->() where m.title='滚滚红尘' return m.rating")
#     print(result)