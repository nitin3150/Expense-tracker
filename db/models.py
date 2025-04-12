from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    groups_created = relationship("Group", back_populates="creator")
    group_memberships = relationship("GroupMember", back_populates="user")
    expenses_paid = relationship("Expense", back_populates="payer")
    expense_splits = relationship("ExpenseSplit", back_populates="user")
    settlements_sent = relationship("Settlement", back_populates="sender", foreign_keys="Settlement.from_user")
    settlements_received = relationship("Settlement", back_populates="receiver", foreign_keys="Settlement.to_user")


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    creator = relationship("User", back_populates="groups_created")
    members = relationship("GroupMember", back_populates="group", cascade="all, delete")
    expenses = relationship("Expense", back_populates="group", cascade="all, delete")


class GroupMember(Base):
    __tablename__ = 'group_members'

    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    joined_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    group = relationship("Group", back_populates="members")
    user = relationship("User", back_populates="group_memberships")


class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
    payer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String)
    date = Column(DateTime(timezone=True), default=func.now())

    # Relationships
    group = relationship("Group", back_populates="expenses")
    payer = relationship("User", back_populates="expenses_paid")
    splits = relationship("ExpenseSplit", back_populates="expense", cascade="all, delete")


class ExpenseSplit(Base):
    __tablename__ = 'expense_splits'

    expense_id = Column(Integer, ForeignKey('expenses.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    owed_amount = Column(Float, nullable=False)

    # Relationships
    expense = relationship("Expense", back_populates="splits")
    user = relationship("User", back_populates="expense_splits")


class Settlement(Base):
    __tablename__ = 'settlements'

    id = Column(Integer, primary_key=True, index=True)
    from_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    to_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    sender = relationship("User", back_populates="settlements_sent", foreign_keys=[from_user])
    receiver = relationship("User", back_populates="settlements_received", foreign_keys=[to_user])