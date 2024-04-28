import { NavLink, NavLinks } from './NavBarStyled.tsx';
import { SideMenuContainer } from './SideNavStyled.tsx';
function SideNav({ isOpen }: { isOpen: boolean }): JSX.Element {
  return (
    <SideMenuContainer isOpen={isOpen}>
      <NavLinks>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/about">About</NavLink>
        <NavLink to="/services">Service</NavLink>
        <NavLink to="/context">Context</NavLink>
      </NavLinks>
    </SideMenuContainer>
  );
}

export default SideNav;
