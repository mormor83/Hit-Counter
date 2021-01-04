from flask_wtf import FlaskForm
from wtforms import  SubmitField


class DBAction(FlaskForm):

    class Meta:
        csrf = True

    reset_hit_count = SubmitField('Reset Count')
