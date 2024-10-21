import { Card } from 'react-bootstrap'
import CardHeader from 'react-bootstrap/esm/CardHeader'

const DisabledCard = ({
  children,
  cardHeight,
}: {
  children: any
  cardHeight?: 'lg' | 'md' | 'sm'
}) => {
  return (
    <Card
      // className="disabled-card-body"
      style={{
        maxHeight:
          cardHeight === 'sm'
            ? '170px'
            : cardHeight === 'md'
            ? '350px'
            : cardHeight === 'lg'
            ? '360px'
            : '200px',
        borderRadius: '30px',
      }}
    >
      {children}
      <div
        className="card-disabled-custom d-flex flex-column align-items-center justify-content-center  "
        style={{
          backgroundColor: 'rgba(0, 0, 0, 0.8)',
          borderRadius: '30px',
        }}
      >
        <p
          className=" h1"
          style={{
            transform: 'rotate(45deg)',
          }}
        >
          Yakında
        </p>
      </div>
    </Card>
  )
}

export default DisabledCard
