from flask import Flask
from data import db_session
from data.jobs import Jobs
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/jobs.db")
    db_sess = db_session.create_session()
    jobs = Jobs()
    jobs.team_leader = '1'
    jobs.job = 'deployment of residential modules 1 and 2'
    jobs.work_size = '15'
    jobs.collaborators = '2, 3'
    jobs.start_date = datetime.now()
    jobs.is_finished = False
    db_sess.add(jobs)
    db_sess.commit()


if __name__ == '__main__':
    main()
