from flask import Flask
import config
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
from exts import db

app = Flask(__name__)
app.config.from_object(config)  # 引入配置文件

app.register_blueprint(cms_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)
db.init_app(app)


if __name__ == '__main__':
    app.run()
