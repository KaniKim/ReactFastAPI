import { useState } from 'react';
import { NavbarContainer, Logo, MenuIcon, NavLinks, NavLink } from './NavBarStyled.tsx';

function NavBar() {
  const [isOpen, setIsOpen] = useState<boolean>(false);

  return (
    <NavbarContainer>
      <Logo>Admin</Logo>
      <MenuIcon onClick={() => setIsOpen(!isOpen)}>
        <div>☰</div>
      </MenuIcon>
      <NavLinks isOpen={isOpen}>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/about">About</NavLink>
        <NavLink to="/services">Service</NavLink>
        <NavLink to="/context">Context</NavLink>
      </NavLinks>
    </NavbarContainer>
  );
}

export default NavBar;
