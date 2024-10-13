import { Link } from 'react-router-dom'
import './header.css'
import {useNavigate} from 'react-router-dom'
import axios from 'axios';

export default function Header(){

    const navigate = useNavigate();

    const username = localStorage.getItem('username');

    function logout(){
        localStorage.removeItem('username');
        localStorage.removeItem('role');
        axios.defaults.headers.common['Authorization'] = '';
        navigate('/')
    }

    return (
        <header>
            <span className='header__title'>
                Недвижимость
            </span>
            <div className='header__login'>
                {
                    username
                    ?
                    <div>
                        <span className='header__username'>{username}</span>
                        <button onClick={logout}>
                            Выйти
                        </button>
                    </div>
                    :
                    <button>
                        <Link to='/login' style={{color: 'var(--white)', textDecoration: 'none'}}>
                            Войти
                        </Link>
                    </button>
                }
            </div>
        </header>
    )
}