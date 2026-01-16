from pydantic import BaseModel, EmailStr, Field, SecretStr, date, model_validator

class UserBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    email: EmailStr

class UserCreate(UserBase):
    name: str | None = None
    email: str
    password: SecretStr = Field(min_length=8, max_length=15)

class UserUpdatePassword(BaseModel):
    current_password: SecretStr = Field(min_length=8, max_length=15)
    new_password: SecretStr = Field(min_length=8, max_length=15)
    confirm_new_password: SecretStr = Field(min_length=8, max_length=15)

    @model_validator(mode="after")
    def validate_password(self):
        if self.new_password != self.confirm_new_password:
            raise ValueError("New password and confirm new password do not match")
        return self

class UserChangePassword(BaseModel):
    current_password: SecretStr = Field(min_length=8, max_length=15)
    new_password: SecretStr = Field(min_length=8, max_length=15)
    confirm_new_password: SecretStr = Field(min_length=8, max_length=15)

    @model_validator(mode="after")
    def validate_password(self):
        if self.new_password != self.confirm_new_password:
            raise ValueError("New password and confirm new password do not match")
        return self
class UserChangeEmail(BaseModel):
    email: EmailStr

    @model_validator(mode="after")
    def validate_email(self):
        if self.email == self.current_email:
            raise ValueError("New email cannot be the same as the current email")
        return self
