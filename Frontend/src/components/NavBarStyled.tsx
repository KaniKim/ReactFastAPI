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
  z-index: 1;
  justify-content: left;
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
  padding-left: 20px;
`;

export const NavLink = styled(Link)`
  color: white;
  text-decoration: none;
  margin-right: 1rem;
  font-size: 20px;
  display: block;
  padding-top: 10px;

  &:hover {
    text-decoration: underline;
  }

  @media (max-width: 768px) {
    padding: 10px;
    border-bottom: 1px solid white;
  }
`;

export const NavLinks = styled.div`
  a {
    color: white;
    text-decoration: none;
    margin-left: 1rem;
    &:hover {
      text-decoration: underline;
    }
  }
  @media (max-width: 768px) {
    display: none;
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
