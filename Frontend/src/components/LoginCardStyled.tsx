import styled from 'styled-components';

export const Container = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

export const LoginContainer = styled.div`
  width: 50%;
  height: 80%;
  position: absolute;
  transform: translate(-50%, -50%);
  top: 55%;
  left: 50%;
  align-items: center;
  justify-content: center;
  background-color: white;

  @media (max-width: 768px) {
    flex-direction: column;
    height: 95%;
  }
`;

export const ImageContainer = styled.div`
  flex: 1;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
`;

export const FormContainer = styled.div`
  flex: 1;
  display: flex;
  width: 90%;
  height: 90%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 16px;
  margin-right: 30px;
  box-shadow: 2px 2px 10px #888888;

  @media (max-width: 768px) {
    margin: 0;
  }
`;
export const Heading = styled.h2`
  font-size: 46px;
`;

export const LoginForm = styled.form`
  width: 90%;
  margin: 30px 0;
  display: flex;
  flex-direction: column;

  @media (max-width: 768px) {
    width: 100%;
  }
`;
export const Label = styled.label`
  font-size: 18px;
  font-weight: 500;
  margin: 10px 0;
`;
export const Input = styled.input`
  width: 100%;
  margin-bottom: 8px;
  padding: 8px;
  margin-bottom: 10px;
  font-size: 16px;
  outiine: none;
`;
export const LoginButton = styled.button`
  color: white;
  width: 60%;
  font-size: 16px;
  padding: 10px 15px;
  margin: 0 auto;
  margin-top: 30px;
  border: none;
  border-radius: 4px;
  background-color: #1575a7;
  cursor: pointer;
  &:hover {
    background-color: #1885c0;
  }
`;
export const CheckBox = styled.input.attrs({ type: 'checkbox' })`
  margin-right: 8px;
`;

export const Paragraph = styled.p`
  font-size: 18px;
  @media (max-width: 768px) {
    font-size: 16px;
  }
`;

export const Anchor = styled.a`
  color: #f78719;
  text-decoration: underline;
  &:hover {
    cursor: pointer;
  }

  ${(props) =>
    props.noLine &&
    css`
      text-decoration: none;
    `}
`;
