
'''
网站搭建主APP
WEB框架
'''
import sys



import web
from dataPro import Question
import sys

#静态界面模板
render = web.template.render('templates/')
#URL处理
urls = ('/', 'index','/add','add')
# web.application实例app
app = web.application(urls, globals())
#知识库的问答接口
que = Question()
print("QA system begin.")

# 处理问题的方法
def dealquestion(question):
    # 查询知识图谱
    answer=que.question_process(question)
    return answer

# 主页显示类
class index:
    def GET(self):
        return render.index()

    def POST(self):
        text=web.input()
        print(text)
        #＃转到‘／’下的页面
        raise web.seeother('/')

# 处理问题类
class add:
    # get方式处理问题
    def GET(self):
        pass

    # post方式处理问题
    def POST(self):
        def enablePrint():
            sys.stdout = sys.__stdout__
        enablePrint()
        text=web.input()
        # 过滤无效post请求
        if text['id']=="bei":
            question=text['q']
            print("接收的问题是",question)
            answer=dealquestion(question)
            print("得到的答案是：",answer)
            if len(str(answer).strip())==0:
                answer="此问题无明确答案"
            print("回答结束")
            return answer
        else:
            pass



if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()