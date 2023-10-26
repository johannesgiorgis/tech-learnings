
interface Club{
  name: string
  logoLocation: string

  isActive(): boolean
}

interface SocccerClub extends Club {
  league: string;
}
