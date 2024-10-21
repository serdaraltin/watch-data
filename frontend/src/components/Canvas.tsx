import React, { useEffect, useRef, useState } from 'react'
import { Button } from 'react-bootstrap'

interface Point {
  x: number
  y: number
}
const imageWidth = 1920
const imageHeight = 1080
const backgroundImage =
  'https://fastly.picsum.photos/id/386/1920/1080.jpg?grayscale&hmac=n4jUJFZs88AE65PawjjO4U2LtoTctNOAhkn_nC5zm3Y'
const Canvas: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null)
  const [points, setPoints] = useState<Point[]>([])
  const [dragPointIndex, setDragPointIndex] = useState<number | null>(null)

  useEffect(() => {
    const canvas = canvasRef.current

    if (canvas) {
      const ctx = canvas.getContext('2d')

      const resizeCanvas = () => {
        canvas.width = window.innerWidth
        canvas.height = (canvas.width * imageHeight) / imageWidth
        ctx?.clearRect(0, 0, canvas.width, canvas.height)
        redraw()
      }

      const drawPoint = (x: number, y: number) => {
        if (ctx) {
          ctx.fillStyle = 'cyan'
          ctx.beginPath()
          ctx.arc(x, y, 6, 0, Math.PI * 2)
          ctx.fill()
        }
      }

      const connectPoints = () => {
        if (ctx && points.length > 1) {
          ctx.strokeStyle = 'magenta'
          ctx.beginPath()
          ctx.moveTo(points[0].x * canvas.width, points[0].y * canvas.height)
          for (let i = 1; i < points.length; i++) {
            ctx.lineTo(points[i].x * canvas.width, points[i].y * canvas.height)
          }
          ctx.closePath()
          ctx.stroke()
        }
      }

      const redraw = () => {
        if (ctx) {
          ctx.clearRect(0, 0, canvas.width, canvas.height)
          points.forEach((point) =>
            drawPoint(point.x * canvas.width, point.y * canvas.height)
          )
          connectPoints()
        }
      }

      const handleMouseDown = (event: any) => {
        const x = event.nativeEvent.offsetX / canvas.width
        const y = event.nativeEvent.offsetY / canvas.height

        // a point is clicked
        for (let i = 0; i < points.length; i++) {
          const point = points[i]
          const dx = x - point.x
          const dy = y - point.y
          if (Math.sqrt(dx * dx + dy * dy) < 5 / canvas.width) {
            setDragPointIndex(i)
            return
          }
        }

        // add a new point
        setPoints((prevPoints) => [...prevPoints, { x, y }])
        console.log(`Point added: x=${x}, y=${y}`)
        redraw()
      }

      const handleMouseMove = (event: any) => {
        if (dragPointIndex === null || !canvas) {
          return
        }

        const x = event.nativeEvent.clientX / canvas.width
        const y = event.nativeEvent.clientY / canvas.height

        // dragged point
        setPoints((prevPoints) => {
          const updatedPoints = [...prevPoints]
          updatedPoints[dragPointIndex] = { x, y }
          return updatedPoints
        })

        console.log(`Point updated: x=${x}, y=${y}`)
        redraw()
      }

      const handleMouseUp = () => {
        setDragPointIndex(null)
      }

      window.addEventListener('resize', resizeCanvas)

      resizeCanvas()

      canvas.addEventListener('mousedown', handleMouseDown)
      canvas.addEventListener('mousemove', handleMouseMove)
      canvas.addEventListener('mouseup', handleMouseUp)

      return () => {
        window.removeEventListener('resize', resizeCanvas)
        canvas.removeEventListener('mousedown', handleMouseDown)
        canvas.removeEventListener('mousemove', handleMouseMove)
        canvas.removeEventListener('mouseup', handleMouseUp)
      }
    }
  }, [canvasRef, points, dragPointIndex])

  return (
    <div>
      <canvas
        ref={canvasRef}
        style={{
          backgroundImage: `url(${backgroundImage})`,
          display: 'block',
          backgroundColor: 'transparent',
          border: '1px solid yellow',
          height: '100%',
          width: '100%',
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat',
        }}
      />
      <Button
        variant={'secondary'}
        className="rounded-pill waves-effect waves-light"
        onClick={() => setPoints((prevPoints) => prevPoints.slice(0, -1))}
      >
        Geri Al
      </Button>
    </div>
  )
}

export default Canvas
