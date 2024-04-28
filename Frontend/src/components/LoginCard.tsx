import { Anchor, CheckBox, Container, FormContainer, Heading, Input, Label, LoginButton, LoginContainer, LoginForm, Paragraph } from './LoginCardStyled.tsx';

function LoginCard() {
  return (
    <LoginContainer>
      <FormContainer>
        <Heading>Login</Heading>
        <LoginForm>
          <Label>Login ID</Label>
          <Input type="text" placeholder="Enter Login ID" />
          <Label>Password</Label>
          <Input type="password" placeholder="Enter Password" />
          <Container>
            <Label>
              <CheckBox name="remember" value="remember" />
              Remember me
            </Label>
            <Anchor>Change Password</Anchor>
          </Container>
          <Label>
            <CheckBox name="role" value="admin" />
            Agree to <Anchor>Terms & Conditions</Anchor>
          </Label>
          <LoginButton>Login</LoginButton>
        </LoginForm>
        <Paragraph>
          Don't have an account? <Anchor>Register Here</Anchor>
        </Paragraph>
      </FormContainer>
    </LoginContainer>
  );
}

export default LoginCard;
