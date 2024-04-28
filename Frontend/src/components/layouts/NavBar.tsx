import { useState } from 'react';
import { NavbarContainer, Logo, MenuIcon } from './NavBarStyled.tsx';
import SideNav from './SideNav.tsx';
import { GiHamburgerMenu } from 'react-icons/gi';

function NavBar() {
  const [isOpen, setIsOpen] = useState<boolean>(false);

  return (
    <NavbarContainer>
      <MenuIcon onClick={() => setIsOpen(!isOpen)}>
        <Logo>
          <GiHamburgerMenu />
        </Logo>
      </MenuIcon>
      <Logo>Admin</Logo>
      <SideNav isOpen={isOpen}></SideNav>
    </NavbarContainer>
  );
}

export default NavBar;
