import sqlalchemy as sa
from sqlalchemy import CHAR, VARCHAR, DATETIME, BOOLEAN
from sqlalchemy.orm import declarative_base, relationship
from app.util import now, uuidgen
from app.config import Config

Base = declarative_base()


# ----------------------------------------------------------------------
# -- Modify the table definitions below to match your database schema --


# Model1Name Model
class Model1Name(Base):
    __Modelname__ = "Model1Names"

    # id = sa.Column(CHAR(64), primary_key=True, nullable=False, default=uuidgen)

    # model1_field1 = sa.Column(VARCHAR, primary_key=True, nullable=False, unique=True)

    # Model2Names = relationship("Model2Name", back_populates="model1_field1")

    # def __repr__(self):
    #     return f"<Model1Name(model1_field1={self.model1_field1})>"


# Model2Name Model
class Model2Name(Base):
    __Modelname__ = "Model2Names"

    # id = sa.Column(CHAR(64), primary_key=True, nullable=False, default=uuidgen)
    # created_at = sa.Column(DATETIME, nullable=False, default=now)
    # updated_at = sa.Column(DATETIME, nullable=True, default=None)
    # is_deleted = sa.Column(BOOLEAN, nullable=False, default=0)

    # model2_field1 = sa.Column(VARCHAR, nullable=False)

    # model1_field1_id = sa.Column(VARCHAR, sa.ForeignKey("Model1Names.model1_field1"), nullable=True)

    # model1_field1 = relationship("Model1Name", back_populates="Model2Names")

    # __Model_args__ = (
    #     sa.UniqueConstraint("model2_field1", "model1_field1_id", name="uq_model2_field1_model1_field1_id"),
    #     sa.Index("ix_id_model2_field1_model1_field1", "id", "model2_field1", "model1_field1_id"),
    # )

    # def __repr__(self):
    #     return f"<Model2Name(id={self.id}, model1_field1={self.model1_field1_id}, model2_field1={self.model2_field1})>"


# ------------------------------------------------------------------
# ------------------------------------------------------------------

db_engine = sa.create_engine(Config.SQLALCHEMY_DATABASE_URI)

# Create Models in the database
Base.metadata.create_all(db_engine)
