import json

from flask import Flask, request

#初始化
app = Flask(__name__,
            #static_path='/static', #表示静态文件的访问路径
            static_url_path='',
            static_folder='static',
            template_folder='template')


#当前程序以调试的模式运行
#======从对象中加载配置======
class Config(object):
    DEBUG=True

app.config.from_object(Config)

# #======从文件中加载配置======
#
# app.config.from_pyfile('config.ini')
#
# #======从环境变量中加载配置====
# app.config.from_envvar()


#使用装饰器路由去与试图函数进行关联
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/demo1')
def demo1():
    return 'ni hao'

#指定请求方式
@app.route('/demo2',methods=['GET','POST'])
def demo2():
    return 'demo2 %s' % request.methods


#给路由添加参数
@app.route('/demo3/<int:user_id>')
def demo3(user_id):
    return 'demo3 %s' % user_id


@app.route('/demo4')
def demo4():
    json_dict={
        "name":"xiaoxi",
        "age":18
    }
    #使用json.dumps将字典转换成JSON字符串，使用json.loads将JSON字符串转换为字典
    result=json.dumps(json_dict)
    return result


if __name__ == '__main__':
    app.run(debug=True)
