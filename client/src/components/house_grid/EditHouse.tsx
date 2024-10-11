import { useState } from "react";
import { HouseProps } from "./House";

type Props = HouseProps & {
    onEdit: (house: HouseProps) => void;
}
export default function EditHouse(props: Props){

    const [title, setTitle] = useState(props.title);
    const [location, setLocation] = useState(props.location);
    const [square, setSquare] = useState(props.square);
    const [price, setPrice] = useState(props.price);
    const [images, setImages] = useState(props.images);

    function handleSubmit(){
        props.onEdit({
            title,
            location,
            square,
            price,
            images,
            url: props.url,
            id: props.id
        })
    }

    return (
        <section id="house_editing">
            <h1>Редактирование жилья</h1>
            <div className="house_editing__property">
                <span>
                    Название
                </span>
                <input type="text" value={title} onChange={e => setTitle(e.target.value)}/>
            </div>
            <div className="house_editing__property">
                <span>
                    Город
                </span>
                <input type="text" value={location} onChange={e => setLocation(e.target.value)}/>
            </div>
            <div className="house_editing__property">
                <span>
                    Площадь, м<sup>2</sup>
                </span>
                <input type="text" value={square} onChange={e => setSquare(e.target.value)}/>
            </div>
            <div className="house_editing__property">
                <span>
                    Цена
                </span>
                <input type="text" value={price} onChange={e => setPrice(e.target.value)}/>
            </div>
            <section id="house_editing__images">
                {
                    images.map((image, i) => (
                        <div key={i}>
                            <img src={image} alt={`${i} image`} />
                            <button onClick={()=>{setImages(prev => prev.filter((_, ind) => ind !== i))}}>
                                <svg focusable="false" viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6zM19 4h-3.5l-1-1h-5l-1 1H5v2h14z" fill="currentColor"></path>
                                </svg>
                            </button>
                        </div>
                    ))
                }
            </section>
            <button id="house_editing__submit" onClick={handleSubmit}>
                Сохранить
            </button>
        </section>
    )
}