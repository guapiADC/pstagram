# -*- encoding=UTF-8 -*-
from pstagram import app,db ,login_manager
from flask import url_for
from sqlalchemy import or_,and_
from flask_script import Manager
from pstagram.models import User,Image,Comment
import random,unittest
manager = Manager(app)


@manager.command
def run_test():
    tests = unittest.TestLoader().discover('./')
    unittest.TextTestRunner().run(tests)
    pass

def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'
@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        db.session.add(User('User'+str(i+1),'a'+str(i)))
        for j in range(0,10):
            db.session.add(Image(get_image_url(),i+1))
            for k in range(0,3):
                db.session.add(Comment('This is a comment'+str(k),1+10*i+j,i+1))
    db.session.commit()

    # '''
    # 更新
    for i in range(0, 100, 3):
        # 通过update函数
        User.query.filter_by(id=i).update({'username': '33新' + str(i)})

    # User.query.filter(User.username.endswith('0')).update({'username': '00新' + User.username}, synchronize_session=False)
    # filter_by多个参数是and
    User.query.filter_by(id=4, password='a4').update({'username': '44牛客新' + str(i)})
    User.query.filter_by(id=5, password='a4').update({'username': '55牛客新' + str(i)})

    for i in range(50,100,2):
        user = User.query.get(i)
        user.username = '[New]'+user.username

    User.query.filter_by(id =50).update({'username':'[New2]'})
    db.session.commit()

    # '''



   # print 2,User.query.get(3)
   # print 3, User.query.filter_by(id=5).first()
   # print 4,User.query.order_by(User.id.desc()).offset(1).limit(2).all()
   # print 5,User.query.filter(User.username.endswith('0')).limit(3).all()
   # print 6,User.query.filter(or_(User.id==88,User.id==99)).all()
   # print 7,User.query.paginate(page=1,per_page=10).items
   # user = User.query.get(1)
   # print 8,user.images
   #image = Image.query.get(1)
   #print 9,image.user





if __name__=='__main__':
    manager.run()