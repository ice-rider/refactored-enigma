import { useEffect, useState } from 'react';

type Props = {
    title: string;
    location: string;
    square: string;
    price: string;
    images: string[];
    url: string;    
    id: number;
}

export type HouseProps = Props

export default function House(props: Props & {onClick: () => void}) {

    const [currentImage, setCurrentImage] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentImage((currentImage + 1) % props.images.length);
        }, 3000);
        return () => clearInterval(interval);
    })

    return (
        <div onClick={() => props.onClick()}>
            <section className="house__images">
                {props.images.map((image, index) => (
                    <img
                        key={index}
                        src={image.includes('http') ? image : `https://www.qctonline.com/wp-content/uploads/qctonline_archives/not_found.png`}
                        alt={props.title}
                        className={index === currentImage ? 'current' : ''}
                        style={{'left': `${(-currentImage + index) * 100}%`}}
                    />
                ))}
            </section>
            <h3 onClick={() => window.open(props.url, '_blank')}>{props.title}</h3>
            <section className="house__property">
                <div className="house__location_icon">
                    <svg className="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium MuiSvgIcon-root MuiSvgIcon-fontSizeMedium svg-icon css-kry165" viewBox="0 0 24 24" fill="orange">
                        <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7m0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5">
                        </path>
                    </svg>
                </div>
                <div>
                    {props.location}
                </div>
            </section>
            <section className="house__property">
                <div style={{fontWeight: 'bold', color: 'orange', fontSize: '2rem', width: '2rem', textAlign: 'center'}}>S</div>
                <div>
                    {props.square} м<sup>2</sup>
                </div>
            </section>
            <div className='price'>{props.price} ₽</div>
        </div>
    )
}