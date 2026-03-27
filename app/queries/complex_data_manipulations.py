from core.database import database
from models import Resumes, Workers, Vacancies


class ComplexDataManipulations:

    @staticmethod
    def bound_vacancies_and_resumes():
        with database.session_factory() as session:
            resume_01 = session.get(Resumes, 1)
            resume_02 = session.get(Resumes, 2)
            vacancy_01 = session.get(Vacancies, 1)
            if (
                resume_01 is not None
                and resume_02 is not None
                and vacancy_01 is not None
            ):
                resume_01.vacancies_replied.append(vacancy_01)
                resume_02.vacancies_replied.append(vacancy_01)

            session.commit()

            # resume_01 = sync_query(Queries.select_resumes_filter_by(id=1))[0]
            # resume_02 = sync_query(Queries.select_resumes_filter_by(id=2))[0]
