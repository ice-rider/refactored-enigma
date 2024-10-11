type LoginFormProps = {
    email: string;
    setEmail: React.Dispatch<React.SetStateAction<string>>;
    password: string;
    setPassword: React.Dispatch<React.SetStateAction<string>>
}
export default function LoginForm(props: LoginFormProps) {

    return (
        <div className="inputs__group">
            <input
                type="email"
                placeholder="Email"
                value={props.email}
                onChange={(e) => props.setEmail(e.target.value)}
            />
            <input
                type="password"
                placeholder="Пароль"
                value={props.password}
                onChange={(e) => props.setPassword(e.target.value)}
            />
        </div>
    )
}