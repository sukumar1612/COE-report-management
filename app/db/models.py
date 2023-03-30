from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

from app.db.schemas import UserLevels, ReportStatus

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    emp_id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    permissions = Column(Enum(UserLevels))


class COE(Base):
    __tablename__ = "coe"

    center_id = Column(String, primary_key=True, index=True)
    center_name = Column(String, index=True)
    establishment_date = Column(Integer, index=True)
    name_and_purpose = Column(String)
    sponsor = Column(String)
    department_name = Column(String)

    department_head = Column(ForeignKey('users.emp_id'))


class Report(Base):
    __tablename__ = "report"

    report_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    report_status = Column(Enum(ReportStatus))
    report = Column(String)
    submission_date = Column(Integer)
    due_date = Column(Integer)

    center_id = Column(ForeignKey('coe.center_id'))