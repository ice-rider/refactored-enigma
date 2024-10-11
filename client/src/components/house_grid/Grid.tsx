import { useEffect, useState } from 'react'
import './grid.css'
import House, {HouseProps} from './House'
import EditHouse from './EditHouse';
import axios from 'axios';

type HouseResponse = {
  "name": string,
  "price": number,
  "location": string,
  "metrs": string | number,
  "image": string[] | null | string,
  "url": string;
  "source": string;
}

export default function Grid(){

    const [data, setData] = useState<HouseProps[]>([]);

    const is_admin = localStorage.getItem('role') === 'admin';

    const [popup_house_index, set_popup_house_index] = useState(-1);

    useEffect(() => {
        axios.get(`/flat/list/abrakadabra`)
        .then(
          res => {
            const fetched_data : HouseResponse[] = res.data.flats;
            setData(fetched_data.filter(item => item.image !== null).map(item => (
                {
                    title: item.name,
                    location: item.location,
                    price: String(item.price),
                    square: String(item.metrs),
                    images: (typeof item.image === 'string' ? [item.image] : item.image) as string[],
                    url: item.url,
                    id: 2
                }
            )))
          }
        )
        .catch(console.log)

    }, 
    [])

    function editHouse(house: HouseProps){
      axios.patch(`/flat/${house.id}`, {
        name: house.title,
        price: house.price,
        location: house.location,
        metrs: house.square,
        image: house.images,
        url: house.url
      })
      .then(res => {
        setData(prev => prev.map((h, i) => (
          i === popup_house_index ? house : h
        )))
      })
      .catch(console.log)

      set_popup_house_index(-1);
    }

    return (
        <main className='houses'>
            <h1>Жилье</h1>
            <section className='house_grid'>
                {
                    data.map((item, index) => <House key={index} {...item} onClick={()=>{set_popup_house_index(index)}}/>)
                }
            </section>
            {
              is_admin && popup_house_index !== -1 &&
              <div id='edit_house_popup' onClick={(e)=>{if(e.target === document.querySelector('#edit_house_popup')) set_popup_house_index(-1)}}>
                <EditHouse {...data[popup_house_index]} onEdit={editHouse} />
              </div>
            }
        </main>
    )    
}