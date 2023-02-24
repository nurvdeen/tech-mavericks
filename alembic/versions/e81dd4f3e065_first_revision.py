"""first revision

Revision ID: e81dd4f3e065
Revises: 
Create Date: 2023-02-24 23:29:04.767926

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e81dd4f3e065'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Inadmin')
    op.drop_table('admin')
    op.drop_table('medications')
    op.drop_table('insurance')
    op.drop_table('test')
    op.drop_table('transactions')
    op.drop_table('immunization')
    op.drop_table('doctors')
    op.drop_table('hospitalWorkers')
    op.drop_table('hospital')
    op.drop_table('allergy')
    op.drop_table('record')
    op.drop_table('patient')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('allergy',
                    sa.Column('allergies', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('hospital_record_id', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('id', sa.VARCHAR(length=200),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['hospital_record_id'], [
                        'record.id'], name='allergy_hospital_record_id_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='allergy_pkey'),
                    sa.UniqueConstraint(
                        'allergies', name='allergy_allergies_key')
                    )
    op.create_table('record',
                    sa.Column('patient', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('type', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=True),
                    sa.Column('DOB', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('BloodType', sa.VARCHAR(length=5),
                              autoincrement=False, nullable=False),
                    sa.Column('Height', sa.DOUBLE_PRECISION(precision=53),
                              autoincrement=False, nullable=False),
                    sa.Column('weight', sa.DOUBLE_PRECISION(precision=53),
                              autoincrement=False, nullable=False),
                    sa.Column('BMI', sa.DOUBLE_PRECISION(precision=53),
                              autoincrement=False, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=200),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(
                        ['patient'], ['patient.id'], name='record_patient_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='record_pkey'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('doctors',
                    sa.Column('id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('speciality', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('hospitalID', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('role', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(
                        ['hospitalID'], ['hospitalWorkers.id'], name='doctors_hospitalID_fkey'),
                    sa.ForeignKeyConstraint(['id'], ['user.id'],
                                            name='doctors_id_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='doctors_pkey'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('immunization',
                    sa.Column('immunziation_name', sa.VARCHAR(
                        length=255), autoincrement=False, nullable=False),
                    sa.Column('immunization_date', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('immunization_location', sa.VARCHAR(
                        length=255), autoincrement=False, nullable=False),
                    sa.Column('hospital_record_id', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('id', sa.VARCHAR(length=200),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['hospital_record_id'], [
                        'record.id'], name='immunization_hospital_record_id_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='immunization_pkey'),
                    sa.UniqueConstraint('immunization_date',
                                        name='immunization_immunization_date_key'),
                    sa.UniqueConstraint('immunization_location',
                                        name='immunization_immunization_location_key'),
                    sa.UniqueConstraint('immunziation_name',
                                        name='immunization_immunziation_name_key')
                    )
    op.create_table('transactions',
                    sa.Column('hospital_record_id', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('doctor_id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('drug_name', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('quantity', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('transaction_amount', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('transaction_type', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('vendor_name', sa.VARCHAR(length=255),
                              autoincrement=False, nullable=False),
                    sa.Column('transaction_date', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=200),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['doctor_id'], [
                        'doctors.id'], name='transactions_doctor_id_fkey', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['hospital_record_id'], [
                        'record.id'], name='transactions_hospital_record_id_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='transactions_pkey'),
                    sa.UniqueConstraint(
                        'drug_name', name='transactions_drug_name_key'),
                    sa.UniqueConstraint(
                        'quantity', name='transactions_quantity_key'),
                    sa.UniqueConstraint('transaction_amount',
                                        name='transactions_transaction_amount_key'),
                    sa.UniqueConstraint('transaction_type',
                                        name='transactions_transaction_type_key'),
                    sa.UniqueConstraint(
                        'vendor_name', name='transactions_vendor_name_key')
                    )
    op.create_table('test',
                    sa.Column('test_name', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('doctor_id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('hospital_record_id', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('id', sa.VARCHAR(length=200),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(
                        ['doctor_id'], ['doctors.id'], name='test_doctor_id_fkey', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['hospital_record_id'], [
                        'record.id'], name='test_hospital_record_id_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='test_pkey'),
                    sa.UniqueConstraint('test_name', name='test_test_name_key')
                    )
    op.create_table('insurance',
                    sa.Column('insuranceID', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=False),
                    sa.Column('name', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=False),
                    sa.Column('address', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=False),
                    sa.Column('phone', sa.VARCHAR(length=60),
                              autoincrement=False, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=200),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='insurance_pkey'),
                    sa.UniqueConstraint(
                        'insuranceID', name='insurance_insuranceID_key'),
                    sa.UniqueConstraint('phone', name='insurance_phone_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('medications',
                    sa.Column('medication_name', sa.VARCHAR(
                        length=128), autoincrement=False, nullable=False),
                    sa.Column('hospital_record_id', sa.VARCHAR(),
                              autoincrement=False, nullable=True),
                    sa.Column('doctor_id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=200),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['doctor_id'], [
                        'doctors.id'], name='medications_doctor_id_fkey', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['hospital_record_id'], [
                        'record.id'], name='medications_hospital_record_id_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='medications_pkey'),
                    sa.UniqueConstraint('medication_name',
                                        name='medications_medication_name_key')
                    )
    op.create_table('user',
                    sa.Column('name', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=False),
                    sa.Column('phone', sa.VARCHAR(length=60),
                              autoincrement=False, nullable=False),
                    sa.Column('email', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=False),
                    sa.Column('password_hash', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=200),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='user_pkey'),
                    sa.UniqueConstraint('email', name='user_email_key'),
                    sa.UniqueConstraint('phone', name='user_phone_key'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('hospital',
                    sa.Column('name', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=False),
                    sa.Column('address', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('phone', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('hospitalID', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=200),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='hospital_pkey'),
                    postgresql_ignore_search_path=False
                    )
    op.create_table('patient',
                    sa.Column('id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('insuranceID', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=True),
                    sa.Column('address', sa.VARCHAR(length=128),
                              autoincrement=False, nullable=False),
                    sa.Column('role', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['id'], ['user.id'],
                                            name='patient_id_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='patient_pkey'),
                    sa.UniqueConstraint(
                        'insuranceID', name='patient_insuranceID_key')
                    )
    op.create_table('admin',
                    sa.Column('id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('hospitalID', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('role', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['hospitalID'], [
                        'hospitalWorkers.id'], name='admin_hospitalID_fkey', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['id'], ['user.id'],
                                            name='admin_id_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='admin_pkey')
                    )
    op.create_table('Inadmin',
                    sa.Column('id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('inusranceID', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('role', sa.VARCHAR(length=50),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['id'], ['user.id'],
                                            name='Inadmin_id_fkey', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['inusranceID'], [
                        'insurance.id'], name='Inadmin_inusranceID_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='Inadmin_pkey')
                    )
    op.create_table('hospitalWorkers',
                    sa.Column('id', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('hospitalID', sa.VARCHAR(),
                              autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('updated_at', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(['hospitalID'], [
                        'hospital.id'], name='hospitalWorkers_hospitalID_fkey', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id', name='hospitalWorkers_pkey')
                    )
    # ### end Alembic commands ###
