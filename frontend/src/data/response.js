const day = {
  result: [
    {
      starttime: '10:00',
      endtime: '11:00',
      timeLabel: '10:00', //bu grafikteki x ekseninde listeleniyor
      totalCustomers: { enter: 51, exit: 60, total: 51 }, //anlık müşteriyi total olarak atıyordu
      maleCustomers: { enter: 0, exit: 0, total: 0 },
      femaleCustomers: { enter: 25, exit: 25, total: 0 },
      average: 0.4594594594594595,
    },
    {
      starttime: '11:00',
      endtime: '12:00',
      timeLabel: '11:00',
      totalCustomers: { enter: 51, exit: 60, total: 51 },
      maleCustomers: { enter: 0, exit: 0, total: 0 },
      femaleCustomers: { enter: 25, exit: 25, total: 0 },
      average: 0.4594594594594595,
    },
    //... Bu şekilde çalışma saatleri aralığı gelirse iyi olur 10:00-22:00 arası 12 obje mesela
  ],
  totalAverage: 212.25, //günlük ortalama müşteri
}

//x ekseni: timeLabel - y ekseni: totalCustomers.total
//üstteki gibi gösterilecek veri neyse 2 datayı array olarak listeliyorum grafikte
// bir array oluşturup vermek zorundayım her bir eksen datasını bundan
//bana dizi halinde atılırsa rahatça maplerim gerekli property i çekerek.

const week = {
  result: [
    {
      starttime: '',
      endtime: '',
      timeLabel: 'Pazartesi',
      totalCustomers: { enter: 51, exit: 60, total: 51 }, //burada günlük total yeterli olur heralde girdi çıktıya gerek yok
      maleCustomers: { enter: 0, exit: 0, total: 0 },
      femaleCustomers: { enter: 25, exit: 25, total: 0 },
      average: 0.4594594594594595,
    },
    {
      starttime: '',
      endtime: '',
      timeLabel: 'Salı',
      totalCustomers: { enter: 51, exit: 60, total: 51 },
      maleCustomers: { enter: 0, exit: 0, total: 0 },
      femaleCustomers: { enter: 25, exit: 25, total: 0 },
      average: 0.4594594594594595,
    },
    //... Bu şekilde 7 günlük bir obje serisi olacak
  ],
  totalAverage: 212.25, //haftalık ortalama müşteri
}
