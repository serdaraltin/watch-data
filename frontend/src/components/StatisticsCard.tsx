import classNames from 'classnames'
import { Card } from 'react-bootstrap'

type StatisticsCard = {
  title: string
  textColorVariation: string
  value: string | number
}

const StatisticsCard = ({
  title,
  value,
  textColorVariation,
}: StatisticsCard) => {
  return (
    <Card>
      <Card.Body>
        <div className="card">
          <div className="card-body widget-user">
            <div className="text-center">
              <h2
                className={classNames('fw-normal text-' + textColorVariation)}
                data-plugin="counterup"
              >
                {value}
              </h2>
              <h5>{title}</h5>
            </div>
          </div>
        </div>
      </Card.Body>
    </Card>
  )
}

export default StatisticsCard
