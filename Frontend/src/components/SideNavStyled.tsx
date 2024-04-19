import styled, { keyframes } from 'styled-components';
const slideIn = keyframes`
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(100%);
  }
`;

const slideOut = keyframes`
  from {
    transform: translateX(100%);
  } 
    to {
        transform: translateX(0);
    }
`;
export const SideMenuContainer = styled.div<{ isOpen: boolean }>`
  height: 100%;
  padding-top: 100px;
  width: 10%;
  top: 0;
  right: 100%;
  position: fixed;
  z-index: -1;
  background-color: #111;
  justify-content: left;
  align-items: center;
  animation-direction: normal;
  animation: ${(props) => (props.isOpen ? slideIn : slideOut)} 0.5s forwards;
`;
