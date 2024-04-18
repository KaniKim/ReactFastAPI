import styled from 'styled-components';
import { Link } from 'react-router-dom';

export const NavbarContainer = styled.nav`
  height: 30px;
  float: left;
  background-color: #333;
  display: flex;
  width: 100%;
  padding: 20px 0 20px 0;
  overflow: auto;
  justify-content: space-between;
  align-items: center;
  color: white;
  flex-direction: row;
  @media (max-width: 768px) {
    flex-direction: column;
    align-items: flex-start;
  }
`;

export const Logo = styled.div`
  font-size: 1.5rem;
  font-family: 'Sans Serif';
`;

export const NavLink = styled(Link)`
  color: white;
  text-decoration: none;
  margin-right: 1rem;

  &:hover {
    text-decoration: underline;
  }

  @media (max-width: 768px) {
    padding: 10px;
    border-bottom: 1px solid white;
  }
`;

export const NavLinks = styled.div<{ isOpen: boolean }>`
  a {
    color: white;
    text-decoration: none;
    margin-left: 1rem;
    &:hover {
      text-decoration: underline;
    }
  }
  @media (max-width: 768px) {
    display: ${(props) => (props.isOpen ? 'flex' : 'none')};
    flex-direction: column;
    width: 100%;
  }
`;

export const MenuIcon = styled.div`
  display: block;
  @media (max-width: 768px) {
    display: block;
    cursor: pointer;
  }
`;
