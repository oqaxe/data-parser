// types.ts
export enum LogLevel {
  DEBUG = 'DEBUG',
  INFO = 'INFO',
  WARN = 'WARN',
  ERROR = 'ERROR',
}

export interface ParsedData {
  [key: string]: any;
}

export interface DataItem {
  id: number;
  timestamp: Date;
  data: ParsedData;
}

export interface Config {
  logLevel: LogLevel;
  dataPath: string;
}

export interface LogMessage {
  timestamp: Date;
  level: LogLevel;
  message: string;
}