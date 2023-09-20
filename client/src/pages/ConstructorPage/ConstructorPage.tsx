
type Props = {}

const ConstructorPage = (_props: Props) => {
  return (
    <div className="constructor">
        <div className="container">
            <h1>Создание модели вручную</h1>
            <div className="form_group">
              <label htmlFor="">Выберите таблицу</label>
              <select name="" id="">
                <option value="ВВП">ВВП</option>
              
              </select>
            </div>
            <div className="form_group">
              <label htmlFor="">Выберите дату</label>
              <select name="" id="">
                <option value="data 1">ДАТА 1</option>
              </select>
            </div>
            <div className="form_group">
              <label htmlFor="">Информация</label>
              <input type="text" placeholder="information" />
            </div>

        </div>
    </div>
  )
}

export default ConstructorPage