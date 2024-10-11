import {useState} from 'react'
import {LoginForm, RegisterForm} from 'components/login'
import './login.css';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';

type LoginResponse = {
    access_token: string;
    user: {
        username: string;
        role: 'admin' | 'user'
    };
}
export default function Login() {

    const navigate = useNavigate()

    const [username, setUsername] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const [code, setCode] = useState('')

    const [step, setStep] = useState(0);

    function loginUser(){
        axios.post(`/login`, {email, password})
        .then((response) => {
            const data : LoginResponse = response.data;
            const {access_token} = data;
            localStorage.setItem('username', data.user.username);
            localStorage.setItem('role', data.user.role);
            axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
            navigate('/')
        })
        .catch((error) => {
            console.log(error)
            toast.error('Неверный логин или пароль')
        })
    }

    function registerUser(){
        axios.post(`/register`, {username, email, password})
        .then((response) => {
            const data : LoginResponse = response.data;
            const {access_token} = data;
            localStorage.setItem('username', data.user.username);
            localStorage.setItem('role', data.user.role);
            axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;
            setStep(2)
        })
        .catch((error) => {
            console.log(error)
            toast.error('Не удалось зарегистрироваться. Проверьте правильность введенных данных')
        })
    }

    function confirmCode(){
        axios.post(`/confirm`, {email, code})
        .then((response) => {
            navigate('/')
        })
        .catch((error) => {
            console.log(error)
            toast.error('Неверный код')
        })
    }

    return (
        <section className='login__container'>
            <div className="login__form">

                {step === 0 && <div className='login__header'>
                    <h1>Войти</h1>
                    <span>
                        Ещё не создали аккаунт?&nbsp;
                    </span>
                    <span className='login__link' onClick={() => setStep(1)}>
                        Зарегистрируйтесь!
                    </span>
                    </div>
                }

                {step === 1 && <div className='login__header'>
                    <h1>Регистрация</h1>
                    <span>
                        Уже есть аккаунт?&nbsp;
                    </span>
                    <span className='login__link' onClick={() => setStep(0)}>
                        Войти!
                    </span>
                    </div>}

                {step === 0 && <LoginForm email={email} setEmail={setEmail} password={password} setPassword={setPassword} />}

                {step === 1 && <RegisterForm 
                email={email} 
                setEmail={setEmail} 
                password={password} 
                setPassword={setPassword} 
                username={username} 
                setUsername={setUsername}
                />}

                {step === 2 && <>
                    <h2>
                        Введите код
                    </h2>
                    <span style={{marginBottom: '10px', fontSize: '0.8rem'}}>
                        На ваш email было отправлено письмо с кодом.
                    </span>
                    <div className='inputs__group'>
                        <input
                            type="text"
                            placeholder="Код"
                            value={code}
                            onChange={(e) => setCode(e.target.value)}
                        />
                    </div>
                </>}
                {
                    step === 0 && <div>
                        <button className='login__button' onClick={loginUser}>
                            Войти
                        </button>
                    </div>
                }

                {
                    step === 1 && <button className='login__button' onClick={registerUser}>
                        Зарегистрироваться
                    </button>
                }

                {
                    step === 2 && <button className='login__button' onClick={confirmCode}>
                        Подтвердить код
                    </button>
                }
            </div>

        </section>
    )
}