import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';

import UsersList from '../UsersList';


const users = [
    {
        'active': true,
        'email': 'danijel1@gmail.com', 'id': 1,
        'username': 'danijel'
    },
    {
        'active': true,
        'email': 'danijel2@gmail.com', 'id': 2,
        'username': 'danijel'
    }
];

test('UsersList renders properly', () => {
    const wrapper = shallow(<UsersList users={users} />);
    const element = wrapper.find('h4');
    expect(element.length).toBe(2);
    expect(element.get(0).props.className).toBe('well');
    expect(element.get(0).props.children).toBe('danijel');
});

test('UsersList renders a snapshot properly', () => {
    const tree = renderer.create(<UsersList users={users}/>).toJSON();
    expect(tree).toMatchSnapshot();
});