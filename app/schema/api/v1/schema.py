from app.app import ma
from app.models import Table1Name, Table2Name

# ...() --> user permission: rw
# ...(dump_only) --> user permission: r
# ...(load_only) --> user permission: w


# -----------------------------------------------------------------------
# -- Modify the schema definitions below to match your database schema --


class Table2NameSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Table2Name
        load_instance = True

    # id = ma.auto_field()
    # model1_field1 = ma.auto_field()


class Table1NameSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Table1Name
        load_instance = True
    
    # # ...(dump_only) --> user permission: Read-only
    # id = ma.auto_field(dump_only=True)
    # created_at = ma.auto_field(dump_only=True)
    # updated_at = ma.auto_field(dump_only=True)
    
    # # ...(load_only) --> user permission: Write-only
    # is_deleted = ma.auto_field(load_only=True)
    
    # # ...(read-write) --> user permission: Read-write
    # model2_field1 = ma.auto_field()
    # model1_field1_id = ma.auto_field()

    # # Adding the relationship to Table2Name
    # model2_field1 = ma.Nested(Table2NameSchema, dump_only=True)
