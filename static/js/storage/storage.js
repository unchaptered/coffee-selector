const getName = () => localStorage.getItem('name');
const removeName = () => localStorage.removeItem('name');

const getToken = () => localStorage.getToken('accessToken');
const removeToken = () => localStorage.removeItem('accessToken');